using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Security.Cryptography;
using System.Globalization;
using System.Diagnostics;

namespace PasswordHandling
{
    public partial class Form1 : Form
    {
        private string hashed_password;
        private const int SaltValueSize = 32;
	private  System.Diagnostics.EventLog appEventLog;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
		string source = "IN618 Example Application";
		string log = "IN618 Log";

		// Check to see if log exists and create it if necessary.
		if (!System.Diagnostice.EventLog.SourceExists(source))
		{
		    appEventLog = new System.Diagnostics.EventLog(log);
		    appEventLog.Source = source;
		}
        }


        private static string GenerateSaltValue()
        {
            StringBuilder builder = new StringBuilder();
            UnicodeEncoding encoding = new UnicodeEncoding();
            byte[] salt = new byte[SaltValueSize];
            RNGCryptoServiceProvider rng = new RNGCryptoServiceProvider();
            rng.GetNonZeroBytes(salt);

            foreach (byte outputByte in salt)
                builder.Append(outputByte.ToString("x2").ToUpper());

            return builder.ToString();
        }



        private static string HashPassword(string clearData, string saltValue, HashAlgorithm hash)
        {
            UnicodeEncoding encoding = new UnicodeEncoding();

            if (clearData != null && hash != null && encoding != null)
            {
                // If the salt string is null or the length is invalid then
                // create a new valid salt value.

                if (saltValue == null)
                {
                    // Generate a salt string.
                    saltValue = GenerateSaltValue();
                }

                // Convert the salt string and the password string to a single
                // array of bytes. Note that the password string is Unicode and
                // therefore may or may not have a zero in every other byte.

                byte[] binarySaltValue = new byte[SaltValueSize];

                binarySaltValue[0] = byte.Parse(saltValue.Substring(0, 2), System.Globalization.NumberStyles.HexNumber, CultureInfo.InvariantCulture.NumberFormat);
                binarySaltValue[1] = byte.Parse(saltValue.Substring(2, 2), System.Globalization.NumberStyles.HexNumber, CultureInfo.InvariantCulture.NumberFormat);
                binarySaltValue[2] = byte.Parse(saltValue.Substring(4, 2), System.Globalization.NumberStyles.HexNumber, CultureInfo.InvariantCulture.NumberFormat);
                binarySaltValue[3] = byte.Parse(saltValue.Substring(6, 2), System.Globalization.NumberStyles.HexNumber, CultureInfo.InvariantCulture.NumberFormat);

                byte[] valueToHash = new byte[SaltValueSize + encoding.GetByteCount(clearData)];
                byte[] binaryPassword = encoding.GetBytes(clearData);

                // Copy the salt value and the password to the hash buffer.

                binarySaltValue.CopyTo(valueToHash, 0);
                binaryPassword.CopyTo(valueToHash, SaltValueSize);

                byte[] hashValue = hash.ComputeHash(valueToHash);

                // The hashed password is the salt plus the hash value (as a string).

                string hashedPassword = saltValue;

                foreach (byte hexdigit in hashValue)
                {
                    hashedPassword += hexdigit.ToString("X2", CultureInfo.InvariantCulture.NumberFormat);
                }

                // Return the hashed password as a string.

                return hashedPassword;
                
            }

            return null;
        }
        private bool VerifyHashedPassword(string password, string profilePassword)
        {
            int saltLength = SaltValueSize * UnicodeEncoding.CharSize;

            if (string.IsNullOrEmpty(profilePassword) ||
                string.IsNullOrEmpty(password) ||
                profilePassword.Length < saltLength)
            {
                return false;
            }

            // Strip the salt value off the front of the stored password.
            string saltValue = profilePassword.Substring(0, saltLength);

            
                HashAlgorithm hash = HashAlgorithm.Create("MD5");
                string hashedPassword = HashPassword(password, saltValue, hash);
                if (profilePassword.Equals(hashedPassword, StringComparison.Ordinal))
                    return true;
           

            // None of the hashing algorithms could verify the password.
            return false;
        }
        private void newPasswordButton_Click(object sender, EventArgs e)
        {
            hashed_password = HashPassword(this.newPasswordBox.Text, null, HashAlgorithm.Create("MD5"));
            newPasswordBox.Text = hashed_password;
        }

        private void passwordCheckButton_Click(object sender, EventArgs e)
        {
            string checkthis = testTextBox.Text;
            if (VerifyHashedPassword(checkthis, hashed_password))
            {
                testTextBox.Text = "Yes";
		appEventLog.WriteEntry("User logged in successfully", System.Diagnostics.EventLogEntryType.Information);

            }
            else
            {
                testTextBox.Text = "No";
		appEventLog.WriteEntry("Login failure, bad password", System.Diagnostics.EventLogEntryType.Information);
            }
        }
    }
}

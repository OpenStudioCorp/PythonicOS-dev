using System;
using System.IO;
using System.Windows.Forms;

namespace FileBrowser
{
    public partial class FileBrowserForm : Form
    {
        private string currentDirectory;

        public FileBrowserForm()
        {
            InitializeComponent();
        }

        private void FileBrowserForm_Load(object sender, EventArgs e)
        {
            currentDirectory = Environment.CurrentDirectory;
            PopulateFileList(currentDirectory);
            currentDirectoryLabel.Text = currentDirectory;
        }

        private void PopulateFileList(string directoryPath)
        {
            fileListBox.Items.Clear();
            try
            {
                // Get the files in the directory
                string[] files = Directory.GetFiles(directoryPath);

                // Add each file to the ListBox with a checkbox
                foreach (string file in files)
                {
                    string fileName = Path.GetFileName(file);
                    fileListBox.Items.Add(fileName, CheckState.Unchecked);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Error: {ex.Message}");
            }
        }

        private void browseButton_Click(object sender, EventArgs e)
        {
            using (FolderBrowserDialog folderBrowserDialog = new FolderBrowserDialog())
            {
                // Show the FolderBrowserDialog
                DialogResult result = folderBrowserDialog.ShowDialog();

                if (result == DialogResult.OK && !string.IsNullOrWhiteSpace(folderBrowserDialog.SelectedPath))
                {
                    currentDirectory = folderBrowserDialog.SelectedPath;
                    PopulateFileList(currentDirectory);
                    currentDirectoryLabel.Text = currentDirectory;
                }
            }
        }

        // Rest of the code...
    }
}

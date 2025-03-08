# False Positive Warning for server manager

## Windows Defender/Antivirus Warning: False Positive

If you're seeing a warning or detection from **Windows Defender** or other antivirus programs when running this script, please **don't worry**—this is a **false positive**.

### Why is this happening?
The script interacts with the file system by creating directories and reading/writing configuration files. Some antivirus software (including Windows Defender) may flag this as suspicious, even though the script is **completely safe**.

There are **no viruses or harmful code** in the script.

### What should you do?
If you trust the script, you can follow these steps to **exclude the script or folder** from being scanned:

#### For Windows Defender:
1. Open **Windows Security** (search for it in the Start menu).
2. Click on **Virus & Threat Protection**.
3. Scroll down and click **Manage Settings** under the Virus & Threat Protection settings.
4. Scroll down to **Exclusions** and click **Add or remove exclusions**.
5. Click **Add an exclusion**, then choose **File** or **Folder**.
6. Select the **script or the folder containing the script**.

#### Submit as a False Positive:
If you think this is a mistake, you can submit the file for review to Microsoft here:  
[Microsoft False Positive Submission](https://www.microsoft.com/en-us/wdsi/filesubmission)

---

### Safety Reminder:
The script is completely safe to use. This warning is simply due to how antivirus software interprets the file system changes the script makes. If you have any concerns, feel free to reach out to us!

Thanks for your understanding!

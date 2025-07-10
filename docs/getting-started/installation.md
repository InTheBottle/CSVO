# Installation

## Pre-Installation

### 1. **Install Dependencies**
   - [Visual C++ x64](https://aka.ms/vs/17/release/vc_redist.x64.exe).
   - [.NET Runtime 8.x.x Desktop x64](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.15-windows-x64-installer).
   - [.NET Runtime 6.0.0 Desktop x64](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-6.0.30-windows-x64-installer).
   - If Visual C++ is installed, use the `Repair` option.

### 2. **Steam Setup**
   - Disable [auto-updates for Skyrim SE](https://help.steampowered.com/en/faqs/view/71AB-698D-57EB-178C#disable).
   - Run Skyrim SE once for graphics check.
   - Install [Creation Kit](https://store.steampowered.com/app/1946180/Skyrim_Special_Edition_Creation_Kit/) on the same drive as Skyrim SE.
   - Run Creation Kit once, select `Yes` to unpack scripts.

### 3. **Install Rare Curios Files** (if you don’t own AE DLC)
   - In Skyrim SE’s Data folder (e.g., `D:\SteamLibrary\steamapps\common\Skyrim Special Edition\data`), delete:
     - `ccbgssse037-curios.bsa`
     - `ccbgssse037-curios.esl`
   - Launch Skyrim SE, go to Creations > Search > Rare Curios > Download.
   - Exit after download (don’t Alt+Tab or verify game files).


## Wabbajack Installation

### 1. **Install Wabbajack**
   - Create a folder (e.g., `C:\Wabbajack`) on your drive’s root (not in Program Files, Desktop, etc.).
   - Download [Wabbajack](https://github.com/wabbajack-tools/wabbajack/releases/latest/download/Wabbajack.exe) and place it in the folder.
   - Run `Wabbajack.exe` (requires version 4.0.0.0 or later).

### 2. **Install CSVO**
   - Open Wabbajack, select Skyrim SE, find CSVO, and click “Download and Install.”
   - Set Installation Location (e.g., `C:\CSVO`) and Downloads Location (avoid Program Files, Desktop, etc.).
   - Click Install.
   - Nexus Premium automates downloads; without it, manually click “Slow Download” for each mod.
   - If successful, proceed to [Post-Installation](post-installation.md). If not, check [Troubleshooting](troubleshooting.md).


.\"C:\Program Files (x86)\VMware\Infrastructure\PowerCLI\Scripts\Initialize-PowerCLIEnvironment.ps1"
# or 
# Import-module VMware.VimAutomation.Core
# Import-module VMware.VimAutomation.Vds
# Import-module VMware.VimAutomation.Cloud
# Import-module VMware.VimAutomation.PCloud
# Import-module VMware.VimAutomation.Cis.Core
# Import-module VMware.VimAutomation.Storage
# Import-module VMware.VimAutomation.HorizonView
# Import-module VMware.VimAutomation.HA
# Import-module VMware.VimAutomation.vROps
# Import-module VMware.VumAutomation
# Import-module VMware.DeployAutomation
# Import-module VMware.ImageBuilder
# Import-module VMware.VimAutomation.License

# AD
Import-Module ActiveDirectory

# 2013 & 2016
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.SnapIn

# 2010
Add-PSSnapin Microsoft.Exchange.Management.PowerShell.E2010

# IIS
Import-Module WebAdministration

# BITS
Import-Module BitsTransfer

# Install NuGet and SQL
Install-Module NuGet, SqlServer

# SQL
Import-Module SqlServer

# Hyper-V
Import-Module Hyper-V
# Import modules
import groupdocs_comparison_cloud
from Common import Common

# Get your client_id and client_secret at https://dashboard.groupdocs.cloud (free registration is required).
Common.client_id = "XXXX-XXXX-XXXX-XXXX"
Common.client_secret = "XXXXXXXXXXXXXXXX"

Common.myStorage = "First Storage"

# Uploading sample test files from local disk to cloud storage
Common.UploadSampleFiles()

# Basic usage Examples

from BasicUsage.GetSupportedFormats import GetSupportedFormats
GetSupportedFormats.Run()
from BasicUsage.GetDocumentInformation import GetDocumentInformation
GetDocumentInformation.Run()
from BasicUsage.CompareDocuments import CompareDocuments
CompareDocuments.Run()
from BasicUsage.CompareDifferentFormats.ComparePdfDocuments import ComparePdfDocuments
ComparePdfDocuments.Run()

# Advanced usage Examples

from AdvancedUsage.CompareMultipleDocuments.CompareMultipleDocumentsOptions import CompareMultipleDocumentsOptions
CompareMultipleDocumentsOptions.Run()
from AdvancedUsage.CompareMultipleDocuments.CompareMultipleProtectedDocuments import CompareMultipleProtectedDocuments
CompareMultipleProtectedDocuments.Run()
from AdvancedUsage.SaveOptions.SetMetadata import SetMetadata
SetMetadata.Run()
from AdvancedUsage.SaveOptions.SetPassword import SetPassword
SetPassword.Run()
from AdvancedUsage.AcceptOrRejectChanges import AcceptOrRejectChanges
AcceptOrRejectChanges.Run()
from AdvancedUsage.CompareProtectedDocuments import CompareProtectedDocuments
CompareProtectedDocuments.Run()
from AdvancedUsage.CompareSensitivity import CompareSensitivity
CompareSensitivity.Run()
from AdvancedUsage.CustomizeChangesStyles import CustomizeChangesStyles
CustomizeChangesStyles.Run()
from AdvancedUsage.GetChangesCoordinates import GetChangesCoordinates
GetChangesCoordinates.Run()
from AdvancedUsage.GetListOfChanges import GetListOfChanges
GetListOfChanges.Run()
from AdvancedUsage.Revisions.GetListOfRevisions import GetListOfRevisions
GetListOfRevisions.Run()
from AdvancedUsage.Revisions.ApplyRevisions import ApplyRevisions
ApplyRevisions.Run()

# Import modules
import groupdocs_comparison_cloud

from Common_Utilities.Utils import Common_Utilities


class Comparison_Python_Copy_Folder:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FolderApi_Instance()
        
        try:
            request = groupdocs_comparison_cloud.CopyFolderRequest("comparisondocs", "comparisondocs1", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.copy_folder(request)
            
            print("Expected response type is Void: 'comparisondocs' folder copied as 'comparisondocs1'.")
        except groupdocs_comparison_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
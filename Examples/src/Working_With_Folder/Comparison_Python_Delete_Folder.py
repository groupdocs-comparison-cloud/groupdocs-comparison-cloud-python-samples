# Import modules
import groupdocs_comparison_cloud

from Common_Utilities.Utils import Common_Utilities


class Comparison_Python_Delete_Folder:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FolderApi_Instance()
        
        try:
            request = groupdocs_comparison_cloud.DeleteFolderRequest("comparisondocs\\comparisondocs1", Common_Utilities.myStorage, True)
            api.delete_folder(request)
            
            print("Expected response type is Void: 'comparisondocs/comparisondocs1' folder deleted recursively.")
        except groupdocs_comparison_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
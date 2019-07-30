# Import modules
import groupdocs_comparison_cloud

from Common_Utilities.Utils import Common_Utilities


class Comparison_Python_Create_Folder:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FolderApi_Instance()
        
        try:
            request = groupdocs_comparison_cloud.CreateFolderRequest("comparisondocs", Common_Utilities.myStorage)
            api.create_folder(request)
            
            print("Expected response type is Void: 'comparisondocs' folder created.")
        except groupdocs_comparison_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
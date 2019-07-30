# Import modules
import groupdocs_comparison_cloud

from Common_Utilities.Utils import Common_Utilities


class Comparison_Python_Delete_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_comparison_cloud.DeleteFileRequest("comparisondocs1\\source.docx", Common_Utilities.myStorage)
            api.delete_file(request)
            
            print("Expected response type is Void: 'comparisondocs1/source.docx' deleted.")
        except groupdocs_comparison_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
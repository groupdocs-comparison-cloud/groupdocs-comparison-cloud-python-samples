# Import modules
import groupdocs_comparison_cloud

from Common_Utilities.Utils import Common_Utilities


class Comparison_Python_Move_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_comparison_cloud.MoveFileRequest("comparisondocs\\source.docx", "comparisondocs1\\source.docx", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.move_file(request)
            
            print("Expected response type is Void: 'comparisondocs/source.docx' file moved to 'comparisondocs1/source.docx'.")
        except groupdocs_comparison_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
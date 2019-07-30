# Import modules
import groupdocs_comparison_cloud

from Common_Utilities.Utils import Common_Utilities


class Comparison_Python_Copy_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_comparison_cloud.CopyFileRequest("comparisondocs\\source.docx", "comparisondocs\\source-copied.docx", Common_Utilities.myStorage, Common_Utilities.myStorage)
            api.copy_file(request)
            
            print("Expected response type is Void: 'comparisondocs/source.docx' file copied as 'comparisondocs/source-copied.docx'.")
        except groupdocs_comparison_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
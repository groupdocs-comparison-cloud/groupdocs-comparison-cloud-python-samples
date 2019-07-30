# Import modules
import groupdocs_comparison_cloud

from Common_Utilities.Utils import Common_Utilities


class Comparison_Python_Upload_File:
    
    @classmethod
    def Run(self):
        # Create instance of the API
        api = Common_Utilities.Get_FileApi_Instance()
        
        try:
            request = groupdocs_comparison_cloud.UploadFileRequest("comparisondocs\\source.docx", "D:\\ewspace\\GroupDocs.Comparison.Cloud.Python.Examples\\src\\Resources\\comparisondocs\\source.docx", Common_Utilities.myStorage)
            response = api.upload_file(request)
            
            print("Expected response type is FilesUploadResult: " + str(response))
        except groupdocs_comparison_cloud.ApiException as e:
            print("Exception while calling API: {0}".format(e.message))
# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to get document info
class GetDocumentInformation:
    @classmethod  
    def Run(cls):
        infoApi = groupdocs_comparison_cloud.InfoApi.from_config(Common.GetConfig())
        
        file_info = groupdocs_comparison_cloud.FileInfo()
        file_info.file_path = "source_files/word/source.docx"

        request = groupdocs_comparison_cloud.GetDocumentInfoRequest(file_info)
        result = infoApi.get_document_info(request)
        print("GetDocumentInformation completed: " + str(result.page_count))
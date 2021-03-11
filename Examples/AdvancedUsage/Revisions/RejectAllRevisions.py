# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to reject all revisions of DOCX document
class RejectAllRevisions:
    @classmethod  
    def Run(cls):
        api_instance = groupdocs_comparison_cloud.ReviewApi.from_config(Common.GetConfig())
        
        source = groupdocs_comparison_cloud.FileInfo()
        source.file_path = "source_files/word/source_with_revs.docx"
        options = groupdocs_comparison_cloud.ApplyRevisionsOptions()
        options.source_file = source
        options.reject_all = True
        options.output_path = "output/result.docx"

        response = api_instance.apply_revisions(groupdocs_comparison_cloud.ApplyRevisionsRequest(options))

        print("Output file link: " + response.href)

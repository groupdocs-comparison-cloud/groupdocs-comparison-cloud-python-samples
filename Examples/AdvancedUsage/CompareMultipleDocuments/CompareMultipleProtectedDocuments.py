# Import modules
import groupdocs_comparison_cloud
from Common import Common

# This example demonstrates how to compare multiple password-protected documents
class CompareMultipleProtectedDocuments:
    @classmethod  
    def Run(cls):
        api_instance = groupdocs_comparison_cloud.CompareApi.from_config(Common.GetConfig())
        
        source = groupdocs_comparison_cloud.FileInfo()
        source.file_path = "source_files/word/source_protected.docx"
        source.password = "1231"
        target = groupdocs_comparison_cloud.FileInfo()
        target.file_path = "target_files/word/target_protected.docx"  
        target.password = "5784"
        target1 = groupdocs_comparison_cloud.FileInfo()
        target1.file_path = "target_files/word/target_1_protected.docx" 
        target1.password = "5784"
        target2 = groupdocs_comparison_cloud.FileInfo()
        target2.file_path = "target_files/word/target_2_protected.docx"                 
        target2.password = "5784"
        options = groupdocs_comparison_cloud.ComparisonOptions()
        options.source_file = source
        options.target_files = [target, target1, target2] 
        options.output_path = "output/result.docx"

        request = groupdocs_comparison_cloud.ComparisonsRequest(options)
        response = api_instance.comparisons(request)
        print("Output file link: " + response.href)
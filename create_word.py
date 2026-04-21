import pypandoc

# Download pandoc if not available
try:
    pypandoc.get_pandoc_path()
except OSError:
    pypandoc.download_pandoc()

# Convert Markdown to DOCX with reference
output = pypandoc.convert_file(
    '/workspaces/prjct2026/analysis.md', 
    'docx', 
    outputfile='/workspaces/prjct2026/project_analysis.docx',
    extra_args=['--reference-doc=/workspaces/prjct2026/reference.docx']
)

print("Word document created with matching style: project_analysis.docx")
from pathlib import Path
from services.pdf_generator_service import PdfGeneratorService
from core.path_handler import PathHandler

path_handler = PathHandler()

PDFS_DIRECTORY: Path = path_handler.get_directory("shared/pdfs")
SHEETS_DIRECTORY: Path = path_handler.get_directory("shared/sheets")

pdf_generator = PdfGeneratorService(f"{PDFS_DIRECTORY}/teste.pdf")

pdf_generator.generate_pdf("teste")

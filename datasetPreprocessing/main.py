import PyPDF2
import os


def get_paper_locations(path: str = "papers",
                        file_extension: str = ".pdf") -> [str]:
    files = os.listdir(path)
    return [f"{path}/{file}" for file in files if file_extension in file]


def load_papers(paper_locations: [str]):
    papers = []
    for paper_location in paper_locations:
        with open(paper_location, 'rb') as file:
            read_pdf = PyPDF2.PdfFileReader(file)
            read_pdf
    return papers

if __name__ == '__main__':
    papers = load_papers(get_paper_locations())
    print(papers)

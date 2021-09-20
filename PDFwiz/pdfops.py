def dateFormat(dstring):
    date = dstring[8:10] + '-' + dstring[6:8] + '-' + dstring[2:6]
    return date


def getNumPages(pdf):
    pages = pdf.numPages
    print(f"The no. of pages in the PDF: {pages}")


def getInfo(pdf):
    info = pdf.documentInfo
    print(f"The detailed information on this PDF is as follows: \n")
    print(f"Author: {info['/Author']}")
    print(f"Producer: {info['/Producer']}")
    print(f"Date Created: {dateFormat(info['/CreationDate'])}")
    print(f"Date Modified: {dateFormat(info['/ModDate'])}")


def getLayout(pdf):
    layout = pdf.pageLayout
    print(f"The page layout used in this PDF is: {layout}")


def getMode(pdf):
    mode = pdf.pageMode
    print(f"The page mode used in this PDF is: {mode}")


def readPage(pdf):
    pagenum = int(input("Which page would you like to read?"))
    page = pdf.getPage(pagenum-1)
    print(f"\nThe content of page number {pagenum} is: \n{page.extractText()}")


def checkEncrypted(pdf):
    if pdf.isEncrypted:
        return True
    return False


opmap = {
    '1': getNumPages,
    '2': getInfo,
    '3': getLayout,
    '4': getMode,
    '5': readPage,
    '6': checkEncrypted
}

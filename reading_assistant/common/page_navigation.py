'''
Created on 2013. 5. 31.


'''
class PageNavigation(object):
    
    def __init__(self, request, totalRowCnt, pageNavigationMaxCnt=5, pageRowCnt=10, curPage=1, startNo=0, lastNo=10):
        if request.GET.has_key('curPage'):
            if int(request.GET['curPage']) > 0:
                curPage = int(request.GET['curPage'])
                startNo = pageRowCnt * (curPage-1)
                lastNo = pageRowCnt * curPage
        
        startPageNo = 1
        lastPageNo = pageNavigationMaxCnt
        
        if curPage > pageNavigationMaxCnt:
            if curPage % pageNavigationMaxCnt > 0:
                startPageNo = ((curPage / pageNavigationMaxCnt) * pageNavigationMaxCnt) + 1
                lastPageNo = (((curPage / pageNavigationMaxCnt) + 1) * pageNavigationMaxCnt)
            else: 
                startPageNo = (((curPage - 1) / pageNavigationMaxCnt) * pageNavigationMaxCnt) + 1
                lastPageNo = ((curPage / pageNavigationMaxCnt) * pageNavigationMaxCnt)
                
        pageNavigationHtml =        '<div align="center" class="pagination">'
        pageNavigationHtml +=           '<ul>'
        
        if(curPage > pageNavigationMaxCnt):
            pageNavigationHtml +=               '<li>'
            pageNavigationHtml +=                   '<a href="javascript:goPage(\'%d\');">Prev</a>' % ((((curPage / pageNavigationMaxCnt) - 1) * pageNavigationMaxCnt) + 1)
            pageNavigationHtml +=               '</li>'
        
        for pageIdx in range(startPageNo, lastPageNo+1):
            #print startPageNo
            #print pageIdx
            #print ((pageIdx - 1)*pageRowCnt)
            if(totalRowCnt > ((pageIdx - 1)*pageRowCnt)):
                if(pageIdx == curPage) :
                    pageNavigationHtml +=               '<li class="active">'
                else :
                    pageNavigationHtml +=               '<li>'
                pageNavigationHtml +=                       '<a href="javascript:goPage(\'%d\');">%d</a>' % (pageIdx, pageIdx)
                pageNavigationHtml +=                   '</li>'
        
        if(totalRowCnt > ((lastPageNo + 1) * pageRowCnt)):
            pageNavigationHtml +=                   '<li>'    
            pageNavigationHtml +=                       '<a href="javascript:goPage(\'%d\');">Next</a>' % ((((startPageNo / pageNavigationMaxCnt) + 1) * pageNavigationMaxCnt) + 1)
            pageNavigationHtml +=                   '</li>'
            
        pageNavigationHtml +=           '</ul>'
        pageNavigationHtml +=       '</div>'
        
        self.request = request
        self.totalRowCnt = totalRowCnt
        self.curPage = curPage
        self.startNo = startNo
        self.lastNo = lastNo
        self.pageNavigationMaxCnt = pageNavigationMaxCnt
        self.pageRowCnt = pageRowCnt
        self.pageNavigationHtml = pageNavigationHtml
def getPR(y_true, y_score):
    pr, rc, thres = metrics.precision_recall_curve(y_true, y_score)
    #print(pr)
    #print(rc)
    #print(thres)
    numpy.seterr(divide='ignore', invalid='ignore')
    f1 = 2*(pr*rc)/(pr+rc) #this F1 disregards threshold
    #updated 20181130
    ap = metrics.average_precision_score(y_true, y_score)
    #f1_from_package = metrics.f1_score(y_true, y_score)
    f1_from_package=None
    f1_max = max(f1)
    max_thres = numpy.nanargmax(f1)
    f1_0 = f1[0]  #The first in the array corresponds to when threshold is 0
    #where all truth are considered predicted
    return(ap, f1_0, f1_max, f1_from_package, max_thres, pr, rc, thres, f1)
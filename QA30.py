#check if the number is positive, negative or zero

def pos_neg_zero(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"

if __name__=="__main__":    
    num=-27
    print(num,"is a",pos_neg_zero(num),"number")
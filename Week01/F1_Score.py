
def f1_score(tp,fp,fn):
    if type(tp) != int or type(fp) != int or type(fn) != int:
        print("Input type must be integer")
        return None
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp, fp and fn must be greater than zero")
        return None
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1_score}")
    
if __name__ == '__main__':
    f1_score(2, 3, 4)
    f1_score('a', 3, 4)
    f1_score(2, 3, 'a')
    f1_score(2,'a',4)
    f1_score(2, 3, 0)
    f1_score(2.1,3,0)
    
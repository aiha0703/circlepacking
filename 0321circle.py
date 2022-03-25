#coding:utf-8
import random as rnd
import rhinoscriptsyntax as rs
class Circle():

    def __init__(self, cPt, r):
        self.cPt = cPt
        self.r = r
    
    def update(self, circles):
        totalMoveVec = [0,0,0]
        for yourCircle in circles:
            if (yourCircle == self):
                continue
            #　衝突判定
            dis = rs.Distance(self.cPt,yourCircle.cPt)
            if(self.r + yourCircle.r > dis):
                # 移動する方向ベクトル
                tmpVec = rs.VectorSubtract(self.cPt, yourCircle.cPt)
                tmpVec = rs.VectorUnitize(tmpVec)
                #移動量
                tmpL = ((self.r + yourCircle.r) - dis)/10
                #移動ベクトル
                moveVec = rs.VectorScale(tmpVec, tmpL)
                #自分を移動
                self.cPt = rs.VectorAdd(self.cPt,moveVec)
    
    def draw(self):
        guids = []
        guid = rs.AddCircle(self.cPt, self.r)
        guids.append(guid)
        return(guids)
    

#num = 100
circles = []
for i in range(num):
    x = rnd.randint(0,12000)
    y = rnd.randint(0,12000)
    z = 0
    r = rnd.randint(1500,3000)
    circle = Circle([x,y,z], r)
    circles.append(circle)


# ASSIGNMENT NO 2  Yeild
# Faizan AShraf MS(CS)  2017-AG-3688

from scipy import stats
from mpl_toolkits.mplot3d import Axes3D
from statsmodels.formula.api import ols
import pandas as pndo
import numpy as num_np
from matplotlib import pyplot as polt
import statsmodels.api as statmode
# Above used the list of libraries

fig = polt.figure()

tech = num_np.array([ 120, 130,150, 160, 170, 180, 190,210])
investment = num_np.array([110,120,110,130,120,120,130,140])
Yield=num_np.array([140,150,150,170,115,125,180,145])
#Here we are going to combine the data
fandg = pndo.DataFrame({
        "Yield": Yield
        , "Technology": tech
        , "investment": investment }
)
display = fig.add_subplot(111, projection='3d')


print("Multiple Linear Regression")
print(fandg)
Reg2 = ols(formula = "Yield ~ tech + investment", data = fandg)
regt = Reg2.fit()
print("RC  and intercept")
print(regt.params)
gt=num_np.array(regt.fittedvalues)


num_items = len(Yield)
mean = sum(Yield) / num_items
#yield Mean Taken Above

differences = [Yield - mean for Yield in Yield]
sq_differences = [d ** 2 for d in differences]
op = num_np.sum(sq_differences)
print('The  TOTAL sum of square(TSS) is =',op)
# above TOTAL SS

d = num_np.array([gt - 60])
jk = num_np.array([d ** 2 for d in d])
ikl = num_np.sum(jk)
print('RSS =',ikl)
# above REGRESSION SS

differences = [Yield - gt]
sq_differences = [d ** 2 for d in differences]
tsd = num_np.sum(sq_differences)
print('Sum of Square of Error (ESS) =.',tsd)
#above ERROR SS

print("R SQUARE is called COEFFICIENT OF DETERMINATION")
print(ikl/op)
#above COEFFICIENT OF DETERMINATION

print(regt.summary())
#Summary of Whole Data
print ("DEtails of ANOVA TABLE")
mod = ols('Yield ~ tech + investment', data=fandg).fit()
aov_table = statmode.stats.anova_lm(mod, typ=2)
print(aov_table)


print(" T Test is taken ")
first=stats.ttest_1samp(tech, 0.0)
print(first)
first=stats.ttest_1samp(investment, 0.0)
print(first)
first=stats.ttest_1samp(Yield, 0.0)
print(first)
#above is Only One Sample T Test

display.scatter(tech,investment,Yield,c='blue',marker='o')
display.set_xlabel("Technology Items ")
display.set_ylabel("Amount of investment")
display.set_zlabel("TYield")
polt.show()
#above Scatter Plot Y vs X
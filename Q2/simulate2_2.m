% step =10
data = importdata("output2-2.txt");
% 数据为L h0 alpha t x1
h0 = data(:,2);
alpha = data(:,3);
L = data(:,1);
t = data(:,4);
x1 = data(:,5);

% 筛选出满足特定条件的数据
idx = (L >= 1000) & (L <= 3000) & (x1 > 0);
L = L(idx);
h0 = h0(idx);
alpha = alpha(idx);
t = t(idx);
x1 = x1(idx);

% 绘制图像
figure
scatter3(h0, alpha, t, 5, L, 'filled')
xlabel('h0')
ylabel('alpha')
zlabel('t')
title('时间t关于h0、α的散点图')
colorbar

% 设置坐标轴和图形的参数
axis tight
view(-50, 30)
colormap(jet)

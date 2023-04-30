% 读取数据
data = load('output3-1.txt');
v = data(:,1);
alpha = data(:,2);
d = data(:,3);
z = zeros(9000);
% 计算d与282.654之差
d_diff = abs(d - 282.654);

% 绘图
scatter3(v, alpha, d_diff,5, 'filled');
hold on;
scatter3(327.49, 45, 0, 'r', 'filled');
hold off;
xlabel('v');
ylabel('α',Rotation=0);
zlabel('|d - 282.65|',Rotation=0);
title('|d - 282.654|与v和alpha');
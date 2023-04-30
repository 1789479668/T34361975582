data = importdata('output-L.txt');

h = data(:,1);
vx = data(:,2);
L = data(:,3);


% 将h和vx合并为一个矩阵
X = [ones(length(h), 1), h, vx, h.^2, vx.^2, h.*vx];

% 拟合模型
b = inv(X'*X)*X'*L;

% 生成一组新的h和vx值
new_h = linspace(min(h), max(h), 100)';
new_vx = linspace(min(vx), max(vx), 100)';
[X1, X2] = meshgrid(new_h, new_vx);
new_X = [ones(length(X1(:)), 1), X1(:), X2(:), X1(:).^2, X2(:).^2, X1(:).*X2(:)];

% 计算拟合值
new_L = reshape(new_X*b, 100, 100);

% 绘制散点图和拟合曲面
scatter3(h, vx, L);
hold on
mesh(X1, X2, new_L);
xlabel('h');
ylabel('vx');
zlabel('L');
title('My Plot');



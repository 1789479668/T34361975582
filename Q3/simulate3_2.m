data = importdata('output3-2.txt');

v = data(:,1);
alpha = data(:,2);
beta = data(:,3);

yyaxis left;
plot(beta,v,'b-');
ylabel('v');

yyaxis right;
plot(beta,alpha,'r-');
ylabel('α')

legend('速度V', '俯冲角度α');
xlabel('风向β');
title('不同风向下最佳姿态对应的V和α图像');
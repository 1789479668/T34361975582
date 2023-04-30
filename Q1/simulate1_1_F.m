data = importdata('output-F.txt');

t = data(:,3);
F = data(:,1);
alpha = data(:,2);

yyaxis left;
plot(t,F,'b-');
ylabel('F');

yyaxis right;
plot(t,alpha,'r-');
ylabel('α')

legend('阻力F大小', 'F与X轴夹角α');
xlabel('时间t');
ylabel('Y轴');
title('My Plot');
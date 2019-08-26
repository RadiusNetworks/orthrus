function [y, n] = angle_filter(x, SOS)
%ANGLE_FILTER Summary of this function goes here
%   Detailed explanation goes here

%na = 1:length(angle_down);

% a=[0.028  0.053 0.071  0.053 0.028];
% b=[1.000 -2.026 2.148 -1.159 0.279];
% angle_fil = filter(b,a,angle);

angle_window = 21;
a=[0.028  0.053 0.071  0.053 0.028];
b=[1.000 -2.026 2.148 -1.159 0.279];

y = sosfilt(SOS,x)/length(x)/50;
% y = movmean(y, angle_window);

n = 1:length(y);

end


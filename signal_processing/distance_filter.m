function [y, n] = distance_filter(x,SOS)
%DISTANCE_FILTER Summary of this function goes here
%   Detailed explanation goes here

distance_window = 5;
y = movmean(x, distance_window);
y = sosfilt(SOS, x)/length(x)/100;
n = 1:length(y);

end


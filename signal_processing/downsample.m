function [yd] = angle_downsample(x, factor)
%ANGLE_DOWNSAMPLE Summary of this function goes here
%   Detailed explanation goes here

% Downsample angle by 16
yd = x(1:factor:end);

end


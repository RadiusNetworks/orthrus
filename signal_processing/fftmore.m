function [Y, f] = fftmore(x, fs)
%ANGLE_FILTER Summary of this function goes here
%   Detailed explanation goes here

L = length(x);
%X = fftshift(abs(fft(x)))/length(x);
X = abs(fft(x)/L);
Y = X(1:floor(L/2)+1);
f = fs*(0:L/2)/L;

end


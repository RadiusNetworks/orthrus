close all;
clear;

% half way through time = 4:42pm
% end time = 4:43pm

% Constant distance(10 meters), varying angle(-50 to 50 deg)

% Load angle and distance data
aoa_data = importdata('sample_data_captures/aoa_samedistance_mintomaxangle.txt',',');
tof_data = importdata('sample_data_captures/tof_samedistance_mintomaxangle.txt',',');
load('angle_coeff.mat');
load('distance_coeff.mat');

fs_distance = 4;                %samples/sec
ts_distance = 1/fs_distance;
fs_angle = 26;                  %samples/sec
ts_angle = 1/fs_angle;

angle = aoa_data.data.';
angle = angle + 50;
for i=1:length(aoa_data.data)
    if (aoa_data.data(i) > 10)
        angle(i) = aoa_data.data(i);
    end
    
end

%Inject 10 hz sinusoid for testing
% n = 1:length(angle);
% sine = 50*sin(2*pi*10*ts_angle*n);
% angle = angle + sine;

angle = downsample(angle, 15);
angle = deg2rad(angle);
[angle_fil, n_ang] = angle_filter(angle, SOS_ANGLE);
[Angle, f_ang] = fftmore(angle, fs_angle);
[Angle_fil, f_ang] = fftmore(angle_fil, fs_angle);

distance = tof_data.data(3:end).';
%distance = interp(distance, 15);
[distance_fil, n_dist] = distance_filter(distance, SOS_DISTANCE);
[Distance, f_dist] = fftmore(distance, fs_distance);
[Distance_fil, f_dist] = fftmore(distance_fil, fs_distance);

polar = distance .* exp(1i * angle(1:length(distance)));
polar_fil = distance_fil .* exp(1i * angle_fil(1:length(distance_fil)));

figure(1)
subplot(4,1,1);
plot(n_ang, rad2deg(angle));
title('Raw Angle');
ylabel('angle(deg)');
xlabel('n(sample)')
subplot(4,1,2);
plot(f_ang, Angle);
title('Raw Angle FFT');
ylabel('angle(deg)');
xlabel('f(hz)')
subplot(4,1,3);
plot(n_dist, distance);
title('Raw Distance');
ylabel('distance(m)');
xlabel('n(sample)')
subplot(4,1,4);
plot(f_dist, Distance);
title('Raw Distance FFT');
ylabel('angle(deg)');
xlabel('f(hz)')

figure(2)
subplot(4,1,1);
plot(n_ang, rad2deg(angle_fil));
title('Filtered Angle');
ylabel('angle(deg)');
xlabel('n(sample)')
subplot(4,1,2);
plot(f_ang, Angle_fil);
title('Filtered Angle FFT');
ylabel('angle(deg)');
xlabel('f(hz)')
subplot(4,1,3);
plot(n_dist, distance_fil);
title('Filtered Distance');
ylabel('distance(m)');
xlabel('n(sample)')
subplot(4,1,4);
plot(f_dist, Distance_fil);
title('Filtered Distance FFT');
ylabel('angle(deg)');
xlabel('f(hz)')

figure(3)
subplot(1,1,1);
compass(polar_fil);
title('Transmitter Position');

% figure(4)
% subplot(1,1,1);
% polarplot(angle_fil(1:length(distance_fil)), distance_fil);
% title('Polar');




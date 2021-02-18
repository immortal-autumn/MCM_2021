% clear all;close all;clc;
% all = vector;
data = Untitled;
data_ping = [31,28,31,30,31,30,31,31,30,31,30,31];
data_run = [31,29,31,30,31,30,31,31,30,31,30,31];

if data(1,1) == 2008 || data(1,1) == 2012 || data(1,1) == 2016
    vector = zeros(length(data),1);
    for i = 1:length(data)
        yue = data(i,2);
        hao = data(i,3);
        temp = 0;
        if yue == 1
            vector(i) = hao;
        else
            temp = 0;
            for j = 1:yue-1
                temp = temp + data_run(j);
            end
            vector(i) = temp + hao;
        end
    end
else
    vector = zeros(length(data),1);
    for i = 1:length(data)
        yue = data(i,2);
        hao = data(i,3);
        temp = 0;
        if yue == 1
            vector(i) = hao;
        else
            temp = 0;
            for j = 1:yue-1
                temp = temp + data_ping(j);
            end
            vector(i) = temp + hao;
        end
    end
end
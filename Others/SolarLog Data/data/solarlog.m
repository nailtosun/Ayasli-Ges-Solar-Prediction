clear all
close all

fileID = fopen('mi160810.bin');
A=fread(fileID,'uint16');
fclose(fileID);

for i=1:171
    asd(i)=A(99*(i-1)+12);
end

plot(asd)
for i = 1:4982    
    if PAC(i) >= 1 && PAC(i) < 5000
        newEncodedVector(i,:) = [0 0 0 0 0 0 0 0 0 0];
    elseif PAC(i) >= 5000 && PAC(i) < 10000
        newEncodedVector(i,:) = [0 0 0 0 0 0 0 0 1 0];
    elseif PAC(i) >= 10000 && PAC(i) < 15000
        newEncodedVector(i,:) = [0 0 0 0 0 0 0 1 0 0];
    elseif PAC(i) >= 15000 && PAC(i) < 20000
        newEncodedVector(i,:) = [0 0 0 0 0 0 1 0 0 0];
    elseif PAC(i) >= 20000 && PAC(i) < 25000
        newEncodedVector(i,:) = [0 0 0 0 0 1 0 0 0 0];
    elseif PAC(i) >= 25000 && PAC(i) < 30000
        newEncodedVector(i,:) = [0 0 0 0 1 0 0 0 0 0];
    elseif PAC(i) >= 30000 && PAC(i) < 35000
        newEncodedVector(i,:) = [0 0 0 1 0 0 0 0 0 0];
    elseif PAC(i) >= 35000 && PAC(i) < 40000
        newEncodedVector(i,:) = [0 0 1 0 0 0 0 0 0 0];
    elseif PAC(i) >= 40000 && PAC(i) < 45000
        newEncodedVector(i,:) = [0 1 0 0 0 0 0 0 0 0];
    else
        newEncodedVector(i,:) = [1 0 0 0 0 0 0 0 0 0];
    end
end
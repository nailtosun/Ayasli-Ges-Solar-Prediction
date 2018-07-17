for i = 1:30354
    if data(i,17) > 0 && data(i,17) < 500
        newEncodedVector(i,:) = [0 0 0 0 0 0 0 0 0 0];
    elseif data(i,17) >= 500 && data(i,17) < 1000
        newEncodedVector(i,:) = [0 0 0 0 0 0 0 0 1 0];
    elseif data(i,17) >= 1000 && data(i,17) < 2500
        newEncodedVector(i,:) = [0 0 0 0 0 0 0 1 0 0];
    elseif data(i,17) >= 2500 && data(i,17) < 5000
        newEncodedVector(i,:) = [0 0 0 0 0 0 1 0 0 0];
    elseif data(i,17) >= 5000 && data(i,17) < 8000
        newEncodedVector(i,:) = [0 0 0 0 0 1 0 0 0 0];
    elseif data(i,17) >= 8000 && data(i,17) < 10000
        newEncodedVector(i,:) = [0 0 0 0 1 0 0 0 0 0];
    elseif data(i,17) >= 10000 && data(i,17) < 12500
        newEncodedVector(i,:) = [0 0 0 1 0 0 0 0 0 0];
    elseif data(i,17) >= 12500 && data(i,17) < 15000
        newEncodedVector(i,:) = [0 0 1 0 0 0 0 0 0 0];
    elseif data(i,17) == 0
        newEncodedVector(i,:) = [0 1 0 0 0 0 0 0 0 0];
    elseif data(i,17) >= 15000 && data(i,17) < 40000
        newEncodedVector(i,:) = [1 0 0 0 0 0 0 0 0 0];
    end
end
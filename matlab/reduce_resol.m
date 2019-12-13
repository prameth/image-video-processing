function[image] = reduce_resol(img, n)

% n is the block size
% image is the reduced resolution image of img

if(n<=0|floor(n)~=n)
    error('Try another n')
endif

[row, col] = size(img);
img = zeros(row, cols);

% nr is the number of rows in nxn square and nc for columns
% rr and rc are the remaining rows and colums

nr = floor(row/n);
rr = mod(row,n);
nc = floor(col/n);
rc = mod(col,n);

sq = n*n;
for i = 1:nr
    for j = 1:nc
        avg = sum(sum(img((1+(i-1)*n) : (i*n), (1+(j-1)*n) : (j*n))))/sq;
        for r = (1+(i-1)*n) : (i*n)
            for c = (1+(j-1)*n) : (j*n)
                image(r, c) = avg;
            endfor
        endfor
    endfor
endfor

sq2 = n * rc;
for i = 1 : Nr
    avg = sum(sum(img((1+(i-1)*n) : (i*n), (1+Nc*n) : cols)))/sq2;
    for r = (1+(i-1)*n) : (i*n)
        for c = (1+nc*n) : col
            image(r, c) = avg;
        endfor
    endfor
endfor

sq3 = n * rr;
for j = 1 : nc
    avg = sum(sum(img((1+nr*n) : row, (1+(j-1)*n) : (j*n))))/sq3;
    for r = (1+nr*n) : row
        for c = (1+(j-1)*n) : (j*n)
            img(r, c) = avg;
        endfor
    endfor
endfor

sq4 = rr*rc;
avg = sum(sum(img((1+nr*n) : row, (1+nc*n) : col)))/sq3;
for r = (1+nr*n) : row
    for c = (1+nc*n) : col
        img(r,c) = avg;
    endfor
endfor

img = uint8(floor(image + 0.5));

endfunction

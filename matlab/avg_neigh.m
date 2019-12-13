function[image] = reduce_resol(img, n)

if(n<0 | floor(n)~=n)
    error('invalid n');
endif

[rows , cols] = size(img);
for i = 1:rows
    for i = 1:cols
        i_lower = max([1, i-n]);
        i_upper = min([rows, i+n]);
        j_lower = max([1, j-n]);
        j_upper = min([cols, j+n]);
        
        img(i, j) = sum( sum( image(i_lower : i_upper, j_lower : j_upper)));
        img(i, j) = img(i, j)/((i_upper - i_lower + 1)*(j_upper - j_lower+1));
    endfor
endfor

image  = uint8(floor(image+0.5));

endfunction

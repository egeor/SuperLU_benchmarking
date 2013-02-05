function create_nd_mat_triplet( n , matrix_name)
% Create ND matrix in triplet format

A = meshsparse (meshnd (n,n));
[i,j,val] = find(A);
data_dump = [i,j,val];
fid = fopen(matrix_name,'w');
rows = size(A,1);
nnzs = size(find(A),1);
fprintf( fid,'%d %d\n', rows, nnzs );
for i=1:nnzs
    fprintf ( fid, '%d %d %f\n', data_dump(i,1), data_dump(i,2), data_dump(i,3));
end
fclose(fid);

end

       
function save_kdf(filename, varagin)
    % check for filename 
    % Overwrite without warning
    if exist(filename, 'file') == 2
        delete(filename);
    end

    % open
    h5create(filename);

    % check length of varagin, if 1
    % treat as a dict-ish thing
    if length(varagin) == 1
        if isstruct(varagin)
            towrite = varagin;  % we'll just write this directly.
        else
            error('Single arguments must be structs');
        end
    else
        % Repack into a key-array pairs into a struct 
        % simplifying the writing code (below)
        vargs = varargin;
        nargs = length(vargs);
        names = vargs(1:2:nargs);
        values = vargs(2:2:nargs);

        towrite = struct();
        for i = 1:length(names)
            towrite.(names(i)) = values(i);
        end
    end

    % iterate over towrite to save as kdf
    keys = fieldnames(towrite)
    for i = 1:length(towrite)
        h5write(filename, keys(i), getfield(towrite, keys(i)));
    end

    % add kdf flag
    h5write(filename, 'kdf', 1);
end


function [data] = load_kdf(filename)
    % check for kdf

    % find the keys

    % load data into a struct
end

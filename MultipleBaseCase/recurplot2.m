function y=recurplot2(x,n)

y=[];
basecase=(1:n);

recur(x);

%Remove adjacent duplicates, there are some issues in running recursive functions in a
%forloop.
y(diff(y)==0)=[];

    function recur(x)
        if ismember(x,basecase)
            y(end+1)=x;
            return
        end
        
        for i=1:n
            y(end+1)=x;
            recur(x-i);
            y(end+1)=x;
        end
        %% Can also set depth of recursion this way.
        
        %         y(end+1)=x;
        %         recur(x-1)
        %         y(end+1)=x;
        %         recur(x-2)
        %         y(end+1)=x;
        %         recur(x-3);
        %         y(end+1)=x;
    end

%% Plotting
plot(y, '-o')
ylabel('X value')
xlabel('Stack Step')
title(strcat('Stack:', num2str(x), '   Base Cases:', num2str(n)))
end


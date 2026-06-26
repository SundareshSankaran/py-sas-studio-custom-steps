/* The following program will utilize the P_[ColumnName] Column from a previous
   Step in order to determine if there is a bias in the dataset using PROC ASSESSBIAS*/

/* Setting up variables for inputTable's libarary and table name */
%let inputLibrary = &inputTable_lib;
%let inputTable = &inputTable_name;

/* Probability Variable Column Selector */
%let probabilityVariable = &probabilityVariable;

/* Target Variable Column Selector and Target Level Dropdown*/
/* Target Level Dropdown has the options of only "Interval" or "Nominal"*/
%let targetVar = &targetVariable;
%let targetLevel = &targetLevel;
%let targetEvent = &targetEvent;

/* Sensistive Variable Column Selector */
%let sensitiveVar = &sensitiveVariable;

/* Setting up variables in Options section */
/* Old school */
%let cutoff = &cutoff;
%let numBins = &numBins;
%let numCuts = &numCuts;
%let selectionDepth = &selectionDepth;
%let weight = &weight;
%let freq = &freq;

/* Setting up fitStat Variables */
%let pVars = &pVars;
%let pEvent = &pEvent;
%let fsDelimiter = &FitStatDelimiter;



proc assessbias 
data=&inputLibrary..&inputTable 
cutoff=&cutoff nBins=&numBins 
nCuts=&numCuts 
selectionDepth=&selectionDepth;
    
      
    /* Input/Probability Variable*/
    var &probabilityVariable;
    
    /* Target Code */
    %if %upcase(&targetLevel)=NOMINAL and %superq(targetEvent) ne %then %do;
        target &targetVar / event=&targetEvent level=&targetLevel;
    %end;
    %else %do;
        target &targetVar;
    %end;    
    
    /*Sensitive Variable */
    sensitivevar &sensitiveVar;
    
    /* Weight (Optional) */
    %if %superq( weight ) ne %then %do;
        weight &weight;
    %end;

    /* Frequency */
    freq &freq;

    
    /* Normalize delimiter value */
    %let fsDelimiterClean=;

    %if %upcase(%superq(FitStatDelimiter)) = %upcase(%str( )) 
        or %superq(FitStatDelimiter) = %nrquote( %(Space%)) %then %do;
        %let fsDelimiterClean=%str( );
    %end;
    %else %if %superq(FitStatDelimiter) = %str(;) %then %do;
        %let fsDelimiterClean=%str(;);
    %end;
    %else %if %superq(FitStatDelimiter) = %str(*) %then %do;
        %let fsDelimiterClean=%str(*);
    %end;
    %else %if %superq(FitStatDelimiter) = %str(.) %then %do;
        %let fsDelimiterClean=%str(.);
    %end;
    %else %if %superq(FitStatDelimiter) = %str(,) %then %do;
        %let fsDelimiterClean=%str(,);
    %end;


    /* Design for fitstat    %if %superq( pVars ) ne and %superq( pEvent ) ne %then %do;
        fitstat pVar=&pVars / pEvent=&pEvent Delimiter = &fsDelimiterClean;
    %end;
    %else %if %superq( pVars ) ne %then %do;
        fitstat pVar=&pVars;
    %end;

    *target &targetVar;
    /*fitstat pVar=&pVars / pEvent=&pEvent Delimiter = &fsDelimiter;
    target &targetVar / event = &targetEvent level = &targetLevel;*/
run;
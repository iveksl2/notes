                                                        Report(s):
* reports drive the dashboard
* can schedule 
where to Find: 
    Reports Tab
    Reports -> create_new_report -> `specify on opportunities, accounts, etc.`.  
    * can add filters
modifying:
    * customize
        * drag in or remove columns by dragging from left hand menu (can drag multiple columns with `Command` key)     
        * good habit to remove unnecessary fields immediately? 
Tabular Report:
    * Disadvantage: Don't allow you to create dashboards and charts
Summary Report:
    * The most common report to create charts and then dashboards
    * drage a field as a 'group by'. Green tick means yes, it can be dropped, Can do up to 3 levels of grouping
Matrix Report
    * similar to summary report, but also allow to group by both rows and columns
    * Typically used when dealing with a large amount of data such as currency 
Joined Report     
    * Usually used to compare 2 or 3 reports side by side  
    * It calls each individual report a `block`
        * once you have chosen a report type cant schoose it again. (Since want to compare across blocks)
        * can only choose from fields within that report. (Color Coded)
        * can choose `Common Fields` (Black) for blue bar across report
        
    
Features 
    Formula Fields: 
        * creating formulas within a column
        * cannot becreated within tabular reports. -> add formula apprears top left    
            * better to go with `all summary` to have a superset of info. (similar to summarize within dplyr after group by)
        * lives within a report
    Bucket Feilds: 
        * allow you to bucket a set of data or range of data togetehr
        * Allow conditionals of columns / fields. Will crete a new field. 
    Report Types:
        * setup -> report type (search) -> click report types -> create new custoemr report type
    Visibility of Reports:
        * decided from folder ( not report itself) 
            * click on blue tack icon. Can give read, write, modify access 
            * If you share with maanger you automatically share those that they manage o
    Schedule:
       within `run report` dropdown -> schedule. (require access to report)
    Export:
        `Export Details` -> csv or excel    
     
       

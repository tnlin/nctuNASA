<?php
class Database 
{
	private static $dbName = '' ; 
	private static $dbHost = '' ;
	private static $dbUsername = '';
	private static $dbUserPassword = '';
	
	private static $cont  = null;
	
	public function __construct() {
		exit('Init function is not allowed');
	}
	
	public static function connect()
	{
	   // One connection through whole application
       if ( null == self::$cont )
       {      
        try 
        {
          self::$cont =  new PDO( 
		"mysql:host=".self::$dbHost.";"."dbname=".self::$dbName, 
		self::$dbUsername, 
		self::$dbUserPassword,
		array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8"));  
        }
        catch(PDOException $e) 
        {
          die($e->getMessage());  
        }
       } 
       return self::$cont;
	}
	
	public static function disconnect()
	{
		self::$cont = null;
	}
}
?>

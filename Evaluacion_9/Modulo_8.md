**Tarea 1: Revisando el rol de IAM para acceder y configurar Amazon Redshift**

Para acceder a la consola de Amazon Redshift, debes tener los permisos apropiados. Este acceso es controlado a través de una política de IAM que se te asigna cuando se lanza el entorno de laboratorio.

Además de tener permisos para usar Amazon Redshift, necesitarás configurar Amazon Redshift para acceder a Amazon S3 en tu nombre. Esto se logra con un rol de IAM, y el rol _MyRedshiftRole_ ha sido proporcionado en el entorno de laboratorio.

En esta tarea, harás lo siguiente:

*   Acceder a IAM y obtener el ARN para el rol de IAM _MyRedshiftRole_.
    
*   Revisar los permisos en la política de IAM administrada _AmazonS3ReadOnlyAccess_.
    
*   Revisar los permisos en la política de IAM _RedshiftIAMLabPolicy_.
    

3.  Acceder al rol de IAM y obtener el Nombre de Recurso de Amazon (ARN).
    
    *   En la Consola de Administración de AWS, en el cuadro de búsqueda a la derecha de **Servicios**, busca y elige **IAM** para abrir la consola de IAM.
        
    *   En el panel de navegación, elige **Roles**.
        
    *   En la lista de roles, busca `MyRedshiftRole` y luego elige el enlace para **MyRedshiftRole** cuando se muestre.
        
        La sección **Resumen** en la parte superior de la página muestra el ARN para el rol.
        
    *   Copia el ARN del rol a un editor de texto para usarlo más tarde.
        
        En la parte inferior de la página, puedes ver qué políticas de permisos están asociadas al rol. Observa que dos políticas de IAM están asociadas a este rol: _AmazonS3ReadOnlyAccess_, que es una política administrada por AWS, y _RedshiftIAMLabPolicy_.
        
4.  Revisar las políticas que están asociadas con el rol.
    
    *   Expande y revisa la política _AmazonS3ReadOnlyAccess_.
        
        Esta política incluye permisos que permiten a Amazon Redshift acceder y leer buckets de S3 y los objetos contenidos en ellos.
        
    *   Ahora expande y revisa la política _RedshiftIAMLabPolicy_.
        
        Esta política fue incluida para que Amazon Redshift pueda describir recursos de Amazon Elastic Compute Cloud (Amazon EC2) y Amazon Virtual Private Cloud (Amazon VPC). Por ejemplo, los permisos en esta política permiten a Amazon Redshift obtener detalles de la configuración de VPC y las subredes asociadas con la VPC, y crear y eliminar una interfaz de red en la VPC.
        

**Resumen de la Tarea 1**

En esta tarea, revisaste un rol que permite a Amazon S3 tener acceso de solo lectura a Amazon Redshift. También revisaste un rol que permite a Amazon Redshift acceder a recursos de Amazon S3, Amazon EC2 y Amazon VPC. Ten estos permisos en mente mientras completas este laboratorio.

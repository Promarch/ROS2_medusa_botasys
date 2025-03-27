from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'serial_port',
            default_value='/dev/ttyUSB0',
            description='Serial port for the Bota FT sensor'
        ),
        
        DeclareLaunchArgument(
            'frame_id',
            default_value='ft_sensor_link',
            description='TF frame ID for the FT sensor measurements'
        ),
        
        DeclareLaunchArgument(
            'publish_rate',
            default_value='10.0',
            description='Rate at which to read the sensor and publish messages (Hz)'
        ),
        
        Node(
            package='bota_ft_sensor',
            executable='bota_ft_sensor_node',
            name='bota_ft_sensor',
            output='screen',
            parameters=[{
                'serial_port': LaunchConfiguration('serial_port'),
                'frame_id': LaunchConfiguration('frame_id'),
                'publish_rate': LaunchConfiguration('publish_rate')
            }]
        )
    ])

#Importar librerias

from OpenGL.GL import *
import glfw

def main():
    width = 400
    height = 600

    if not glfw.init():
        return
    #declarar ventana
    window = glfw.create_window(width, height, 'mi ventana', None, None)
    #configuraciones de opengl
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    #verificar creacion de la ventana
    if not window:
        glfw.terminate()
        return
    #establecer el contexto
    glfw.make_context_current(window)
    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)
    #ciclo de dibujo(draw loop)
    while not glfw.window_should_close(window):
        #estblacer el viewport
        glViewport(0,0,width,height)
        #establecer el color de lo borrado
        glClearColor(0.5, 0.5, 0.5,1.0)
        #borrar el contenido del viewport 
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #dibujar
        #queda pendiente
        #polling de inputs
        glfw.poll_events()
        #cambiar los buffers
        glfw.swap_buffers(window)
    #acabar con procesos y usp de memoria
    glfw.destroy_window(window)
    glfw.terminate()

#ejecutar el main 
if __name__ == '__main__':
    main()



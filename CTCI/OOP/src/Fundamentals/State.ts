enum ToolType {
  SELECTION,
  BRUSH,
  ERASER
}

class Canvas {
  currentTool: ToolType;

  mouseDown(): void {
    switch (this.currentTool) {
      case ToolType.SELECTION:
        console.log('Selection Icon');
        return;
      case ToolType.BRUSH:
        console.log('Brush Icon');
        return;
      case ToolType.ERASER:
        console.log('Eraser Icon');
        return;
      default:
        throw new Error('Incorrect Tool Type');
    }
  }

  mouseUp(): void {
    switch (this.currentTool) {
      case ToolType.SELECTION:
        console.log('Selection Icon');
        return;
      case ToolType.BRUSH:
        console.log('Brush Icon');
        return;
      case ToolType.ERASER:
        console.log('Eraser Icon');
        return;
      default:
        throw new Error('Incorrect Tool Type');
    }
  }

  getCurrentTool(): ToolType {
    return this.currentTool;
  }

  setCurrentTool(newTool: ToolType) {
    this.currentTool = newTool;
  }
}
